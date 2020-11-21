
запуск
```
pip install -r requirements.txt
python3 run.py
```

создание товаров
```
curl -X POST -H "Content-Type: application/json" --data '{"name": "iphone19", "description": "style is better then money"}' http://localhost:5000/goods/ 
curl -X POST -H "Content-Type: application/json" --data '{"name": "iphone20", "description": "7D photo", "parameters": {"screen": "4.9"}}' http://localhost:5000/goods/ 
curl -X POST -H "Content-Type: application/json" --data '{"name": "redmi", "description": "red price", "parameters": {"accum": "6h", "screen": "5.0"}}' http://localhost:5000/goods/ 
curl -X POST -H "Content-Type: application/json" --data '{"name": "nexus", "description": "5G communication"}' http://localhost:5000/goods/ 
curl -X POST -H "Content-Type: application/json" --data '{"name": "elephone", "description": "better tommorow then never", "parameters": {"accum": "6h", "screen": "4.9"}}' http://localhost:5000/goods/ 
```
посмотреть все товары
```
curl http://localhost:5000/goods/
```

фильтрация по имени, параметрам
```
curl http://localhost:5000/goods/?name=iphone20
curl http://localhost:5000/goods/?name=redmi
curl http://localhost:5000/goods/?accum=6h
curl http://localhost:5000/goods/?screen=4.9
curl "http://localhost:5000/goods/?screen=4.9&accum=6h"
```

информация о товаре по его id (или 404 если его нет)
```
curl "http://localhost:5000/goods/5fb8cf0e3a12c31d9aad7073"
```

удалить все
```
curl -X DELETE http://localhost:5000/goods/
```
