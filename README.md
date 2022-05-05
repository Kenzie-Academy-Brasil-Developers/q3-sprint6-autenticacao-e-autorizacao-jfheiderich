### ENDPOINTS:
####Método | Endpoint
- POST /api/signin
- POST /api/signup
- GET /api
- PUT /api
- DELETE /api/id


### SIGNUP <font color=blue>V1 e V2</font>


- <font color=lime>POST</font> /api/signup - Formato da requisição:

```py
{
    "name": "John",
    "last_name": "Wick",
    "email": "johnwick@gmail.com",
    "password": "BabaYaga"
}
```
 #### RESPOSTA - <font color=LIME>201  CREATED</font>
```py
{
    "name": "John",
    "last_name": "Wick",
    "email": "johnwick@gmail.com"
}
```
#### REQUISIÇÕES ERRADAS PARA - <font color=lime>POST</font> /api/signup:

#### - CASO:  KEYS ERRADAS 
- <font color=lime>POST</font> /api/signup 

```py
{
    "NOME": "John",
    "last_name": "Wick",
    "email": "johnwick@gmail.com",
    "password": "BabaYaga"
}
```
#### RESPOSTA - <font color=red>400  BAD REQUEST</font>

``` py
{
	"error": {
		"valid_keys": [
			"name",
			"last_name",
			"email",
			"password"
		],
		"key_sended": "NOME"
	}
}
```
#### - CASO:   NAME JÁ EXISTENTE 
- <font color=lime>POST</font> /api/signup 
```py
{
    "name": "John",
    "last_name": "Wick",
    "email": "johnwick@gmail.com",
    "password": "BabaYaga"
}
```
#### RESPOSTA - <font color=ORANGE> 409 CONFLICT</font>

```py
{
	"error": "User alredy exists"
}
```

### SIGNIN <font color=blue>V1</font>


- <font color=lime>POST</font> /api/signin - Formato da requisição:
```py
{
    "email": "johnwick@gmail.com",
    "password": "BabaYaga"
}
```
#### RESPOSTA - <font color=LIME> 200 OK</font>
```py
{
    "api_key": "370e63d575b6c1bfb973b0b61047dae3"
}
```
### SIGNIN <font color=blue>V2</font>


- <font color=lime>POST</font> /api/signin - Formato da requisição:
```py
{
    "email": "johnwick@gmail.com",
    "password": "BabaYaga"
}
```
#### RESPOSTA - <font color=LIME> 200 OK</font>
```py

{
	"token": 
    "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY1MTc3NjIyMSwianRpIjoiYzdjZDExNTYtZWU2ZS00NjRkLWFiNGYtMGRiMjljZWY3Mzk4IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6eyJuYW1lIjoiSm9objMiLCJsYXN0X25hbWUiOiJXaWNrIiwiZW1haWwiOiJqb2hud2lja0BnbWFpbC5jb20ifSwibmJmIjoxNjUxNzc2MjIxLCJleHAiOjE2NTE3NzcxMjF9.ZvX-YHoLboLT-CdiDZIgAy_G1nJfXLr3pCng6h85Q4o"
}

```



### LISTA DE USUÁRIOS <font color=blue>V1 e V2</font>
<font color=yellow>Rota Protegida por Token</font>
- <font color=purple>GET</font> /api:


#### RESPOSTA - <font color=LIME> 200 OK</font>
```py
{
    "name": "John",
    "last_name": "Wick",
    "email": "johnwick@gmail.com"
}
```
### ATUALIZAR USUÁRIO <font color=blue>V1 e V2</font>
<font color=yellow>Rota Protegida por Token</font>
- <font color=orange>PUT</font>/api - Formato da requisição:
```py
{
    "name": "John",
    "last_name": "Wick II",
    "email": "johnwick@gmail.com",
    "password": "Matrix"
}
```
#### RESPOSTA - <font color=LIME> 200 OK</font>
```py
{
    "name": "John",
    "last_name": "Wick II",
    "email": "johnwick@gmail.com"
}
```
### DELETAR USUÁRIO <font color=blue>V1 e V2</font>
<font color=yellow>Rota Protegida por Token</font>
- <font color=red>DELETE</font> /api/id:
#### RESPOSTA - <font color=LIME> 200 OK</font>
```py
{
    "msg": "User John has been deleted."
}
```


