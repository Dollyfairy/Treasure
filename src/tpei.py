import pandas as pd
import matplotlib.pyplot as plt


quantity = [['玻璃', 2], ['塑膠', 1], ['紙容器', 1], ['鐵鋁', 1], ['電池', 1]]

df = pd.DataFrame(
    quantity,
    columns=['country', 'pop'])

plt.pie(df['pop'], labels=df['country'], autopct='%1.2f%%')

plt.title('Population')
# plt.savefig("src/static/Pie.jpg")
plt.show()
