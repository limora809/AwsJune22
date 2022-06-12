import re
import boto3
import json
import matplotlib.pyplot as plt
import os

print(os.environ)


branch_name = 'answers/alonit'
bucket_name = 'alonitbucket2022'


with open('questions/compute.md') as f:
    x = f.read()


answers = {}

for q in x.split('\n\n'):
    f = re.findall(r'^\s+\d+', q)
    if f:
        q_num = int(f[0])
        s = re.search(f'.*\*\*.*\*\*.*', q)
        if s is not None:
            f2 = re.findall(r'\d+', s.group(0))
            if f2:
                answers[q_num] = int(f2[0])

s3_client = boto3.client('s3')

s3_client.download_file('alonitbucket2022', 'answers.json', 'answers.json')

with open('answers.json') as f:
    x = json.load(f)

if branch_name not in x:
    x[branch_name] = {
        'compute': [None] * 29
    }

for q, a in answers.items():
    x[branch_name]['compute'][q-1] = a

s3_client.upload_file('answers.json', bucket_name, 'answers.json')


def draw_votes_hist(name, lst):
    plt.figure(figsize=(3.2, 2.4))
    plt.bar([f'A{l[0]}' for l in lst], [l[1] for l in lst], color='maroon', width=0.4)

    # plt.xlabel("Courses offered")
    # plt.ylabel("No. of students enrolled")
    # plt.title("Students enrolled in different courses")
    # plt.show()
    plt.savefig(f'compute.png')
    s3_client.upload_file('compute.png', bucket_name, f'compute{name}.png',
                          ExtraArgs={
                              'ACL': 'public-read',
                              'ContentType': 'image/png'
                          })


for i in range(1, 30):
    votes = {1: 0, 2: 0, 3: 0, 4: 0}
    for vote in x.values():
        answer = vote['compute'][i - 1]
        if answer is None:
            continue
        if answer not in votes:
            votes[answer] = 0
        votes[answer] += 1

    draw_votes_hist(i, sorted(votes.items(), key=lambda x: x[0]))

