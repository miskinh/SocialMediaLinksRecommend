if __name__ == "__main__":
    for user in Users.select():
  print user.username

    nim = Users.select().where(Users.username == 'Nim').get()
    print nim.username

    tom = Users.select().where(Users.username == "Tom").get()
    print tom.username

    document = Documentcontents.create(
  documentid = 1000,
  sparsewords = "SPARSE WORDS",
  text = "Text",
  topics = "Topics",
  url = "URL"
    )

    for document in Documentcontents.select():
  print document.text