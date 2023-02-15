import re

fname = 'data/ga_3.dat'

# pattern = r"AvgFitness: (\d+\.\d+)"
pattern = r"Score: (\d+)"

fnames = [
    'hc_ds_',
    'hc_ss_',
    'hc_pn_',
    'ts_ds_',
    'ts_ss_',
    'ts_pn_',
    'ga_',
]

for file in fnames:
    for i in range(1, 4):
        with open(f'data/{file}{i}.dat', 'r') as f:
            data = f.readlines()
        if file == 'ga_':
            # grabbing fitness
            f = open(f'extracted/{file}{i}.dat', 'w')
            for line in data:
                match = re.search(r' Fitness: (\d+)', line)
                if match:
                    f.write(f'{int(match.group(1))}\n')
                else:
                    break
            f.close()
            # grabbing average
            f = open(f'extracted/{file}{i}_avg.dat', 'w')
            for line in data:
                match = re.search(r'AvgFitness: (\d+\.\d+)', line)
                if match:
                    f.write(f'{float(match.group(1))}\n')
                else:
                    break
            f.close()

        else:
            f = open(f'extracted/{file}{i}.dat', 'w')
            for line in data:
                match = re.search(pattern, line)
                if match:
                    f.write(f'{int(match.group(1))}\n')
                else:
                    break
            f.close()


# with open(fname, 'r') as f:
#     lines = f.readlines()

# for line in lines:
#     match = re.search(pattern, line)
#     if match:
#         print(float(match.group(1)))
#     else:
#         exit()