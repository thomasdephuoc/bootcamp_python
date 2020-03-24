import getopt, sys, time

def ft_progress(lst):
    for i in lst:
        progress = float(i/len(lst))
        progress_bar = ""
        for j in range(int(progress * 25)):
            if j > 0:
                progress_bar += "="
        progress_bar += ">"
        print(f'ETA: {time.perf_counter()/max(0.01, progress):5.2f}s [{progress * 100:3.0f}%] [{progress_bar:24s}] {i}/{len(lst)} | elapsed time {time.perf_counter():5.2f}s')
        yield i 

listy = range(3333)
ret = 0
for elem in ft_progress(listy):
    ret += elem
    time.sleep(0.005)
print()
print(ret)