def main():
    faker = Faker()
    for _ in range(10):
        for j in range(random.randint(1, 10)):
            user = User.objects.get(id=random.choice([1, 2, 3, 5, 6]))
            post = Post.objects.create(author=user, title=faker.company(), content=faker.text(),
                                       published=datetime.now().strftime("%Y-%d-%m"), is_active=True)
            post.save()


if __name__ == '__main__':
    import os

    from django.core.wsgi import get_wsgi_application

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
    application = get_wsgi_application()

    import random

    from faker import Faker

    from blog.models import Post, User
    from django.utils.timezone import datetime

    main()
