from rest_framework.pagination import PageNumberPagination


class SmallSetPagination(PageNumberPagination):
    """
    Pagination class for splitting a request in smaller parts
    """

    # url parameter for page number
    page_query_param = "p"
    # page size
    page_size = 6
    # url parameter for alternate page size
    page_size_query_param = "ps"
    # if ps=??>=max_page_size => ps=10
    max_page_size = 10
