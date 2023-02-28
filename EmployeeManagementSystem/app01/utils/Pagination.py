class Pagination(object):
    def __init__(self, request, data_list, page_size=3, params="index", sub=2):
        page_index = int(request.GET.get(params, 1) if request.GET.get(params, 1) != '' else 1)
        self.page_index = page_index
        self.page_size = page_size

        self.data_start = (page_index - 1) * page_size
        self.data_end = page_index * page_size

        self.query_list = data_list[self.data_start, self.data_end]
