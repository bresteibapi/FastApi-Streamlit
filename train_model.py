import numpy as np
import joblib
from sklearn.linear_model import LinearRegression

# Генерация случайных данных для обучения
X = np.random.rand(100, 2)
y = 3 * X[:, 0] + 2 * X[:, 1] + np.random.randn(100)  # Пример линейной зависимости

# Создание и обучение модели
model = LinearRegression()
model.fit(X, y)

# Сохранение модели на диск
joblib.dump(model, 'model.joblib')
