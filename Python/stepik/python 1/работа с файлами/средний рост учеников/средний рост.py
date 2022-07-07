classes = {i: 0 for i in range(1, 12)}
cl_stu_cnt = [0 for i in range(11)]

with open('dataset_3380_5.txt', 'r', encoding='utf-8') as txt:

    for line in txt.readlines():
        clss, name, height = line.strip().split('\t')
        clss, height = int(clss), int(height)

        cl_stu_cnt[clss - 1] += 1
        classes[clss] = (classes[clss] * (cl_stu_cnt[clss - 1] - 1) + height) / cl_stu_cnt[clss - 1]

with open('asnwer.txt', 'w', encoding='utf-8') as txt:
    for i in classes:
        if classes[i] == 0:
            classes[i] = '-'
        txt.write(f'{i} {classes[i]}\n')
        print(i, classes[i])
