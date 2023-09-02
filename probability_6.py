from matplotlib import pyplot as plt

def show():
    fig = plt.gca()
    fig.axes.get_xaxis().set_visible(False)
    fig.axes.get_yaxis().set_visible(False)
    plt.show()


plt.figure(figsize=(10, 10))

plt.text(0.01, 0.9, "Овечкин за 1 игру кидает 5 шайб. За 1200 матчей 600 голов.", fontsize=15)
plt.text(0.01, 0.8, "Найти математическое ожидание за 100 матчей.", fontsize=15)
plt.text(0.01, 0.7, "Для начала найдем вероятность попаданий:", fontsize=15)
form = r"$p = 600/1200 = 0,5 * 100 = 50(голов)"
plt.text(0.01, 0.6, form, fontsize=15)
plt.text(0.01, 0.5, "Дальше расчитаем вероятности для всех 5 бросков:", fontsize=15)
form = r"$x_i = 0; 1; 2; 3; 4; 5$"
plt.text(0.01, 0.4, form, fontsize=15)
form = r"$p_i = 0,5; 0,25; 0,125; 0,0625; 0,03125; 0,03125$"
plt.text(0.01, 0.3, form, fontsize=15)
plt.text(0.01, 0.2, "Теперь вычислим математическое ожидание и дисперсию:", fontsize=15)
form = r"$M(X) = \sum x_i*p_i = 0,96875$"
plt.text(0.01, 0.1, form, fontsize=15)
form = r"$D(X) = \sum x_i^2*p_i-(M(X))^2 = 3,03$"
plt.text(0.01, 0.01, form, fontsize=15)

show()