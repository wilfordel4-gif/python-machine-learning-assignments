from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt
x=[[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]]
y=[30,40,45,55,65,70,80,85,90,95]
model=LinearRegression()
model.fit(x,y)
user_input =input("Enter hours studied: ")
hours_studied = float(user_input)
predicted_score = model.predict([[hours_studied]])
print(f"Predicted score: {predicted_score[0]:.2f}")
plt.scatter(x, y, color='red', linestyle='--', label='Actual Data')
x_line = np.linspace(1, 10, 100).reshape(-1, 1)
y_line = model.predict(x_line)
plt.plot(x_line, y_line, color='red',linestyle='-', label='Regression Line')
plt.scatter(hours_studied, predicted_score, color='blue', label='Predicted Score')
plt.xlabel('Hours Studied')
plt.ylabel('Examination Score')
plt.title('Relationship Between Hours Study and Exam Score')
plt.legend()
plt.grid()
plt.show()