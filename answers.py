def get_topics(review):
    system_prompt = """
    You are an experienced customer service representative for a large online retailer. Your task is to extract a list of the main topics mentioned in a customer review. Extract up to 5 topics. If no topics exists in the review return an empty list.

    Return the response as a json in this format:
    {
        "topics": [list of extracted topics]
    }
    """

    user_prompt = f"""
    Please extract the topics mentioned in the following review which also includes the title:

    {review}
    """
    completion = get_completion(system_prompt, user_prompt)
    completion = json.loads(completion)
    return completion["topics"]


for ind, row in reviews.iterrows():
    review = row[["title", "review"]].to_dict()
    topics = get_topics(review)
    reviews.loc[ind, "topics"] = str(topics)
