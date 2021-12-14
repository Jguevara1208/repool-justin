/*
Repool Challenge: Implementation Sample 
In the language of your choice, please implement the following specifications to the best of your  ability. If there’s extra features you add, or things you avoid because they’re unnecessarily hard  in your language of choice, let us know in a comment or readme of your submission. 
Single User, Single Machine, Non-persisted Transactional Key  Value Store 

Write a program that implements the following six functions, with the corresponding behavior shown in the examples

Transactions are controlled with BEGIN, COMMIT, and ROLLBACK.  
BEGIN starts a new transaction. Transactions may be nested. 
COMMIT ends a transaction  and commits the new values. 
ROLLBACK ends the transaction and throws out the new values.  
Values SET within a transaction are visible within the transaction 

SET <key> <value> 
GET <key>  
SUM 
BEGIN 
COMMIT  
ROLLBACK  

 ##### Example 1 ##### 
 [{a: 5}, {a: 5, foobar: memes2}]
SET a 5  
GET a  
> 5  
BEGIN  
GET a  
> 5  
SET a bar 
GET a
> bar 
SET foobar memes  
GET foobar  
> memes  
ROLLBACK  
GET a  
> 5  
GET foobar  
> NULL  
BEGIN  
SET foobar memes2  
GET a
> 5
COMMIT  
GET a
> 5
GET foobar  
> memes2  

##### Example 2 ##### 

SET a 5  
BEGIN  
SET a 6  
BEGIN  
SET a 7 
SET b 9 
GET a  
> 7  
COMMIT 
GET a  
> 7 
GET b
> 9 
ROLLBACK  
GET a  
> 5
GET b
> NULL  
ROLLBACK  
> Error: Not in a transaction  
*/

const stack = [{}, [{}]]


const set = (key, value) => {
    const current = stack[stack.length - 1]
    current[key] = value
}

const get = (key) => {
    const current = stack[stack.length - 1]
    return current[key]
}

const sum = () => {
    const current = stack[stack.length - 1]
    const values = Object.values(current)
    const sum = values.reduce((sum, val) => {
        if (!(+val.isNaN())) sum += +val
        return sum
    }, 0)
    return sum
}

const begin = () => {
    const newObj = {}

    stack.push(newObj)
}

const commit = () => {
    stack.pop()
    stack.pop()
    stack.push(current)
}

const rollback = () => {
    stack.pop()
}