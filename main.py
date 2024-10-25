import vk_api
import time

access_token = 'vk1.a.RaayURQlSrh4ixOZohffEhtJ0K8ociQsel6eNMoSVJLn6hqlKNVXQ53oNoUrRN-XS_zikmePUV0S1VVU1YC8JKh4IaYDuEMEDPzVcVHIUIhqAxuxlvTZPIB1XAMirOw3GGsVhWhr6Y7f6aXykyIXAqdu2HEIQaekjjjr7nMNPwrXtr_5-0-3hz6vUJM_c8iden_m63xDP5BjaZZ0jFECTw'

group_id = 218375169

vk_session = vk_api.VkApi(token=access_token)
vk = vk_session.get_api()

def get_all_posts(group_id, count=100):
    posts = []
    offset = 0
    while True:
        print(f"Получаем посты с offset = {offset}")
        response = vk.wall.get(owner_id=-group_id, count=count, offset=offset)
        posts.extend(response['items'])
        offset += count
        if len(response['items']) == 0:
            break
        time.sleep(0.33)
    return posts

def get_comments_for_post(post_id, group_id):
    comments = []
    offset = 0
    count = 100
    while True:
        print(f"Получаем комментарии для поста {post_id} с offset = {offset}")
        response = vk.wall.getComments(owner_id=-group_id, post_id=post_id, count=count, offset=offset)
        comments.extend(response['items'])
        offset += count
        if len(response['items']) == 0:
            break
        time.sleep(0.33)
    return comments

def count_comments_with_keyword(comments, keyword):
    count = 0
    for comment in comments:
        if keyword.lower() in comment['text'].lower():
            count += 1
            print(f"Найдено {count} комментариев со словом '{keyword}'")
    return count

posts = get_all_posts(group_id)

keyword = "энвилоуп"
post_keyword_comment_counts = {}
total_keyword_mentions = 0

for post in posts:
    print(f"Обрабатываем пост ID {post['id']}")
    comments = get_comments_for_post(post['id'], group_id)
    count = count_comments_with_keyword(comments, keyword)
    post_keyword_comment_counts[post['id']] = count
    total_keyword_mentions += count

for post_id, count in post_keyword_comment_counts.items():
    print(f"Пост ID {post_id}: {count} комментариев со словом '{keyword}'")

print(f"Общее количество комментариев со словом '{keyword}' во всех постах: {total_keyword_mentions}")
