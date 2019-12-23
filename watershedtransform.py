def detection(V, E, im):
    INIT = 0
    label = []
    for p in D:
        label[p] = INIT
    curent_label = 1
    fifo_init(queue)
    for p in V:
        if label[p] == INIT:
            label[p] = curent_label
            fifo_add(p, queue)
        while not fifo_empty(queue):
            s = fifo_remove(queue)
            for q in Ng(s):
                if im[s] == im[q]:
                    if label[q] == INIT:
                        label[q] = curent_label
                        fifo_add(q,queue)
        curent_label += 1

    return label
