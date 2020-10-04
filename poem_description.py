def poem_description(publishing_date, author, title, original_work):
	poem_desc = "The poem {title} by {author} was originally published in {original_work} in {publishing_date}.".format(publishing_date=publishing_date, author=author, title=title, original_work=original_work)
	return poem_desc
