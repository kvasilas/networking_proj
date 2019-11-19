import numpy as np
import matplotlib.pyplot as plt


host = np.loadtxt(r'C:\Users\USER\Documents\coding\projects\networking_proj\density_monitor\data\number_host.txt', delimiter=",", unpack=False)
ip = np.loadtxt(r'C:\Users\USER\Documents\coding\projects\networking_proj\density_monitor\data\number_ip.txt', delimiter=",", unpack=False)
x = np.loadtxt(r'C:\Users\USER\Documents\coding\projects\networking_proj\density_monitor\data\numbers.txt', delimiter=",", unpack=False)

def plot_totals(x, y, label):
    plt.plot(x, y, 'b.-', label='Hosts')
    plt.ylim(55,110)
    plt.xlim(1,168)
    plt.xticks(np.arange(0, 169, step=24))#data points + 1
    plt.xlabel('Hours')
    plt.ylabel(label)
    plt.title(label + ' on a Network over a week')
    
    plt.annotate('Monday', xy=(8, 55))
    plt.annotate('Tuesday', xy=(32, 55))
    plt.axvspan(24, 48, alpha=0.3, color='red')
    plt.annotate('Wednesday', xy=(54, 55))
    plt.annotate('Thursday', xy=(79, 55))
    plt.axvspan(72, 96, alpha=0.3, color='red')
    plt.annotate('Friday', xy=(106, 55))
    plt.annotate('Saturday', xy=(128, 55))
    plt.axvspan(120, 144, alpha=0.3, color='red')
    plt.annotate('Sunday', xy=(154, 55))
    
    plt.grid(True)
    plt.legend()

    plt.show()

def plot_averages(y, label):
    x_lab = ['00:00', '01:00', '02:00', '03:00', '04:00', '05:00', '06:00',
             '07:00', '08:00', '09:00', '10:00', '11:00', '12:00', '13:00',
             '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00',
             '21:00', '22:00', '23:00', '24:00']
    plt.plot(calc_avg(y), 'b-', label='Hosts')
    plt.xticks(np.arange(0, 24, step=1), x_lab)#data points + 1
    plt.xlim(0, 23)
    plt.xlabel('Hours')
    plt.ylabel(label)
    plt.title('Hourly Average ' + label + ' on a Network')

    plt.grid(True)
    plt.legend()

    plt.show()

def calc_avg(x):
    avgs = []
    hour_start = 0
    hour_sum = 0
    for j in range(0, 24, 1):
        for i in range(hour_start, 169, 24):
            hour_sum += x[i]
            #print(i)
        hour_sum /= 7
        avgs.append(hour_sum)
        hour_start += 1
        hour_sum = 0
    avgs[0] *= 7
    avgs[0] /= 8
    np.asarray(avgs)
    return(np.asarray(avgs))


def main():
    #plot_totals(x, host, "Hosts")
    plot_totals(x, ip, "IP Addresses")
    #plot_averages(host, "Hosts")
    plot_averages(ip, "IP Addresses")

main()
