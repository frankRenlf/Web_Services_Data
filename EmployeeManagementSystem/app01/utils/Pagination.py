import math

from django.utils.safestring import mark_safe


class Pagination(object):
    def __init__(self, request, data_list, search='id', page_size=3, params="index", sub=2):
        self.page_index = int(request.GET.get(params, 1) if request.GET.get(params, 1) != '' else 1)
        mobile_txt = request.GET.get(search)
        self.search = search
        self.mobile_txt = mobile_txt if mobile_txt is not None else ''
        self.page_index = self.page_index
        self.page_size = page_size

        self.data_start = (self.page_index - 1) * page_size
        self.data_end = self.page_index * page_size

        self.number_list = data_list[self.data_start: self.data_end]

        self.total_page_nums = math.ceil(data_list.count() / page_size)
        self.sub = sub
        self.page_list = []
        self.html()

    def html(self):
        first = max(self.page_index - self.sub, 1)
        self.page_list.append('<li class=""><a href="?index={}&{}={}" aria-label="Previous">'
                              '<span aria-hidden="true">First</span></a></li>'.format(1, self.search, self.mobile_txt))
        if self.page_index == 1:
            self.page_list.append('<li class="disabled"><a href="?{}={}" aria-label="Previous">'
                                  '<span aria-hidden="true">«</span></a></li>'.format(self.search, self.mobile_txt))
        else:
            self.page_list.append('<li class=""><a href="?index={}&{}={}" aria-label="Previous">'
                                  '<span aria-hidden="true">«</span></a></li>'.format(self.page_index - 1, self.search,
                                                                                      self.mobile_txt))
        end = min(self.page_index + self.sub, self.total_page_nums)
        for i in range(first, end + 1):
            if i == self.page_index:
                self.page_list.append(
                    '<li class=active><a href="?index={}&{}={}">{}</a></li>'.format(i, self.search, self.mobile_txt, i))
            else:
                self.page_list.append(
                    '<li><a href="?index={}&{}={}">{}</a></li>'.format(i, self.search, self.mobile_txt, i))
        if self.page_index == self.total_page_nums:
            self.page_list.append('<li class="disabled"><a href="?index={}&{}={}" aria-label="Next">'
                                  '<span aria-hidden="true">»</span></a></li>'.format(self.page_index, self.search,
                                                                                      self.mobile_txt))
        else:
            self.page_list.append('<li class=""><a href="?index={}&{}={}" aria-label="Next">'
                                  '<span aria-hidden="true">»</span></a></li>'.format(self.page_index + 1, self.search,
                                                                                      self.mobile_txt))
        self.page_list.append('<li class=""><a href="?index={}&{}={}" aria-label="Previous">'
                              '<span aria-hidden="true">End</span></a></li>'.format(self.total_page_nums, self.search,
                                                                                    self.mobile_txt))
        self.page_list.append("""
                    <form method="get">
                    <div class="input-group" style="width: 200px">
                        <input type="text" name="index" class="form-control" placeholder="page number">
                        <span class="input-group-btn">
                        <button class="btn btn-default" type="submit">jump</button>
                    </span>
                    </div>
                </form>
                """)
        self.page_list = mark_safe("".join(self.page_list))