from django_filters import FilterSet, DateTimeFromToRangeFilter
from django_filters.widgets import DateRangeWidget, RangeWidget
from .models import Post


class PostFilter(FilterSet):
    dateCreation = DateTimeFromToRangeFilter(lookup_expr=(
        'icontains'), widget=RangeWidget(attrs={'type': 'datetime-local'}))

class Meta:
    model = Post
    fields = ('author', 'dateCreation', 'categoryType')