
# Chapter_ 1 Introduction

users = [
  { "id" : 0, "name" : "Hero"},
  { "id" : 1, "name" : "Dunn"},
  { "id" : 2, "name" : "Sue"},
  { "id" : 3, "name" : "Chi"},
  { "id" : 4, "name" : "Thor"},
  { "id" : 5, "name" : "Clive"},
  { "id" : 6, "name" : "Hicks"},
  { "id" : 7, "name" : "Devin"},
  { "id" : 8, "name" : "Devin"},
  { "id" : 9, "name" : "Klein"},
]

friendship_pair = [ 
                    (0,1), (0,2), (1,2), (1,3), (2,3), (3,4), 
                    (4,5), (5,6), (5,7), (6,8), (7,8), (8,9)
                  ]

friendships = {user["id"] : [] for user in users}
for i,j in friendship_pair:
  friendships[i].append(j) # Add j as a friend of user i
  friendships[j].append(i) # Add i as a friend of user j
  
# print(friendships) # {0: [1, 2], 1: [0, 2, 3], 2: [0, 1, 3], 3: [1, 2, 4], 4: [3, 5], 5: [4, 6, 7], 6: [5, 8], 7: [5, 8], 8: [6, 7, 9], 9: [8]}

def number_of_friends(user):
  global friendships
  '''How many friends does user have?'''
  user_id = user["id"]
  friend_ids = friendships[user_id]
  return len(friend_ids)

total_connections = sum(number_of_friends(user) for user in users)
# print(total_connections) # 24

num_users = len(users)
# print(num_users) # 10

avg_connections = total_connections / num_users
# print(avg_connections) # 2.4

# Sorting the most friends people and least friends people
num_friends_by_id = [(user['id'], number_of_friends(user)) for user in users]
# print(num_friends_by_id) # [(0, 2), (1, 3), (2, 3), (3, 3), (4, 2), (5, 3), (6, 2), (7, 2), (8, 3), (9, 1)]

num_friends_by_id.sort(key=lambda id_and_friends : id_and_friends[1], reverse=True) # Sorting largest to smallest

# print(num_friends_by_id) # [(1, 3), (2, 3), (3, 3), (5, 3), (8, 3), (0, 2), (4, 2), (6, 2), (7, 2), (9, 1)]

def foaf_ids_bad(user) -> object:
  """foaf is short for "friend of a friend" """
  return [foaf_id
          for friend_id in friendships[user['id']]
          for foaf_id in friendships[friend_id]]
# for usr in users:
#   print(foaf_ids_bad(usr))

from collections import Counter

def friends_of_friends(user):
  user_id = user["id"]
  return Counter(
    foaf_id
    for friend_id in friendships[user_id]   # for each of my friends
    for foaf_id in friendships[friend_id]   # find their friends
    if foaf_id != user_id                   # who aren't me
    and foaf_id not in friendships[user_id] # and aren't my friends
  )

# print(friends_of_friends(users[3]))


# List of data with pairs of (user_id, interest)
interests = [
  (0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"), (0, "Spark"), (0, "Storm"), (0, "Cassandra"),
  (1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"), (1, "Postgres"),
  (2, "Python"), (2, "scikit learn"), (2, "scipy"), (2, "numpy"), (2, "statsmodels"), (2, "pandas"), 
  (3, "R"), (3, "Python"), (3, "statistics"), (3, "regression"), (3, "probability"), 
  (4, "machine learning"), (4, "regression"), (4, "decision trees"), (4, "libsvm"), 
  (5, "Python"), (5, "R"), (5, "Java"), (5, "C++"), (5, "Haskell"), (5, "programming languages"), 
  (6, "statistics"), (6, "probability"), (6, "mathematics"), (6, "theory"), 
  (7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"), (7, "neural networks"), 
  (8, "neural networks"), (8, "deep learning"), (8, "Big Data"), (8, "artificial intelligence"), 
  (9, "Hadoop"), (9, "Java"), (9, "MapReduce"), (9, "Big Data")
]

def data_scientists_who_like(target_interest) -> list:
  """Find the ids of all users who like the target interest.
  
  return-> list of ID's of user who have the {target_interest} field of interest"""
  return [user_id
          for user_id, user_interest in interests
          if user_interest == target_interest]
# print(data_scientists_who_like("Python"))

# ! Not ideal for large searches ______^

from collections import defaultdict

# Keys are interests, values are lists of users_dis with that
user_ids_by_interest = defaultdict(list)

for user_id, interest in interests:
  user_ids_by_interest[interest].append(user_id)
  
# print(user_ids_by_interest)
# Now opposite
# Keys are user_ids, values are lists of interests for that user_id
interests_by_user_id = defaultdict(list)

for user_id, interest in interests:
  interests_by_user_id[user_id].append(interest)
  
# print(interests_by_user_id)

def most_common_interest_with(user):
  return Counter(
    interested_user_id
    for interest in interests_by_user_id[user['id']]
    for interested_user_id in user_ids_by_interest[interest]
    if interested_user_id != user['id']
  )
# print("Printing most common interests...")
my_usr = users[0]
# print(f"The users in common with the user having id {my_usr['id']} and name {my_usr['name']} are : ")
common_with_usr = most_common_interest_with(my_usr)

for _id, interest_count in common_with_usr.items():
  usr = [usr for usr in users if usr['id'] == _id][0]
  # print(f"The user with id {usr['id']} and name {usr['name']} have {interest_count} interests in common with {my_usr['name']}")


# ! ======================= Salaries and Experience =======================

salaries_and_tenures = [(83000, 8.7), (88000, 8.1), (48000, 0.7), (76000, 6), (69000, 6.5), (76000, 7.5), (60000, 2.5), (83000, 10), (48000, 1.9), (63000, 4.2)]


# Extracting Avg salary for each tenure

# keys are years, values are lists of the salaries for each tenure
salary_by_tenure = defaultdict(list)
for salary, tenure in salaries_and_tenures:
  salary_by_tenure[tenure].append(salary)
# print(salary_by_tenure)

# keys are years, each value is average salary for that tenure
average_salary_by_tenure = {
  tenure: sum(salaries) / len(salaries)
  for tenure, salaries in salary_by_tenure.items()
}
print(average_salary_by_tenure)

# As there are no same tenure, we will bucket the tenures:

def tenure_bucket(tenure):
  if tenure < 2:
    return "less than two"
  elif tenure < 5:
    return "between two and five"
  else:
    return "more than five"

# Grouping salaries

# Keys are tenure buckets, values are lists of salaries for that bucket
salary_by_tenure_bucket = defaultdict(list)

for salary, tenure in salaries_and_tenures:
  bucket = tenure_bucket(tenure)
  salary_by_tenure_bucket[bucket].append(salary)

# Now computing average salary for each group

# Keys are tenure buckets, values are average salary for that bucket
average_salary_by_bucket = {
  tenure_bucket : round(sum(salaries) / len(salaries), 2)
  for tenure_bucket, salaries in salary_by_tenure_bucket.items()
}

print(average_salary_by_bucket)
