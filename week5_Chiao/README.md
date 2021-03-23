# 第五周作業 

## 要求二:建立資料庫和資料表

### 1. 建立一個新的資料庫，取名字為website。
![2-1](https://user-images.githubusercontent.com/76685877/112131682-c6eb4f80-8c04-11eb-8f74-b7d00c35290f.png)

 
### 2. 在資料庫中，建立資料表，取名字為user。資料表中必須包含以下欄位設定：
![2-2](https://user-images.githubusercontent.com/76685877/112131686-c783e600-8c04-11eb-8bac-5a77ec1db9ad.png)
![2-2-1](https://user-images.githubusercontent.com/76685877/112131687-c81c7c80-8c04-11eb-819a-909fce62d509.png)
![2-2-2](https://user-images.githubusercontent.com/76685877/112131689-c8b51300-8c04-11eb-83a5-24c26b5e1455.png)


 
 
 ## 要求三：基本的 SQL 指令


### 1. 使用 INSERT 指令新增一筆資料到 user 資料表中，這筆資料的 username 和password 欄位必須是 ply。接著繼續新增至少 4 筆隨意的資料。
![3-1](https://user-images.githubusercontent.com/76685877/112131691-c8b51300-8c04-11eb-8b4a-5054c2b9e17d.png)
![3-1-1](https://user-images.githubusercontent.com/76685877/112131692-c94da980-8c04-11eb-9198-0429c8f4aad0.png)
![3-1-2](https://user-images.githubusercontent.com/76685877/112131697-c9e64000-8c04-11eb-9c38-0a1a49cfa309.png)

 
 
 
### 2. 使用 SELECT 指令取得所有在 user 資料表中的使用者資料。
![3-2](https://user-images.githubusercontent.com/76685877/112131698-ca7ed680-8c04-11eb-87b7-50408db1db3a.png)

 
### 3. 使用 SELECT 指令取得 user 資料表中總共有幾筆資料。
![3-3](https://user-images.githubusercontent.com/76685877/112131700-cb176d00-8c04-11eb-9abe-2a15253855da.png)

 
### 4. 使用 SELECT 指令取得所有在 user 資料表中的使用者資料，並按照 time 欄位，由近到遠排序。
![3-4](https://user-images.githubusercontent.com/76685877/112131701-cb176d00-8c04-11eb-8453-9f4cbe7a4b66.png)

 
### 5. 使用 SELECT 指令取得 user 資料表中第 2 ~ 4 共三筆資料，並按照 time 欄位，由近到遠排序。
![3-5](https://user-images.githubusercontent.com/76685877/112131703-cbb00380-8c04-11eb-919e-ff52f7df2b34.png)

 
### 6. 使用 SELECT 指令取得欄位 username 是 ply 的使用者資料。
![3-6](https://user-images.githubusercontent.com/76685877/112131704-cbb00380-8c04-11eb-8885-cbfe8742bc4b.png)

 
### 7. 使用 SELECT 指令取得欄位 username 是 ply、且欄位 password 也是 ply 的資料。
![3-7](https://user-images.githubusercontent.com/76685877/112131708-cc489a00-8c04-11eb-9e6f-acf6444e925d.png)

 
### 8. 使用 UPDATE 指令更新欄位 username 是 ply 的使用者資料，將資料中的 name 欄位改成【丁滿】。
![3-8](https://user-images.githubusercontent.com/76685877/112131711-cc489a00-8c04-11eb-8f3b-7e3373691d45.png)


### 9. 使用 DELETE 指令刪除所有在 user 資料表中的資料。
![3-9](https://user-images.githubusercontent.com/76685877/112131712-cce13080-8c04-11eb-8e49-c7381412e26c.png)



 ## 要求四：結合資料表 SQL JOIN 的操作 (Optional)

 
### 1. 在資料庫中，建立新資料表，取名字為message。資料表中必須包含以下欄位設定：
![4-1](https://user-images.githubusercontent.com/76685877/112131715-cce13080-8c04-11eb-8f3f-0756bcc2ab93.png)

 

### 2. 使用 SELECT 搭配 JOIN 的語法，取得所有留言，資料中須包含留言會員的姓名。
![4-2](https://user-images.githubusercontent.com/76685877/112131716-cd79c700-8c04-11eb-9599-098a16e29778.png)
![4-2-1](https://user-images.githubusercontent.com/76685877/112131718-cd79c700-8c04-11eb-9bac-189a420f504c.png)
![4-2-2](https://user-images.githubusercontent.com/76685877/112131719-ce125d80-8c04-11eb-849d-8d0f3fc6c77a.png)
![4-2-3](https://user-images.githubusercontent.com/76685877/112131720-ce125d80-8c04-11eb-877e-e0365cf4774d.png)
![4-2-4](https://user-images.githubusercontent.com/76685877/112131722-ceaaf400-8c04-11eb-8ba1-d8a72336fb85.png)

 
 
### 3. 使用 SELECT 搭配 JOIN 的語法，取得 user 資料表中欄位 username 是 ply 的所有留言，資料中須包含留言會員的姓名。

![4-3](https://user-images.githubusercontent.com/76685877/112131723-cf438a80-8c04-11eb-8552-9c037285f6d2.png)
 

