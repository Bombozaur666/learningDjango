from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from .models import Post

class LatestPostFeed(Feed):
    title = 'mojblog'
    link = '/blog'
    description = 'Nowe posty kazdego dnia'

    def items(self):
        return Post.published.all()[:5]
    def iteam_title(self,item):
        return item.title
    def iteam_describtion(self,item):
        return truncatewords(item.body, 30)