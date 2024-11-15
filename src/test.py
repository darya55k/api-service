import pickle
import json

# Загрузите модель
with open("./model.pkl", "rb") as f:
    model = pickle.load(f)

# Получите список всех атрибутов модели
attributes = dir(model)

# Сохраните атрибуты в текстовом формате
with open("model_attributes.txt", "w") as f:
    json.dump(attributes, f, indent=4)

print("Атрибуты модели сохранены в 'model_attributes.txt'")