class SortField:
    SORT_DIR_ASC = 'asc'
    SORT_DIR_DESC = 'desc'

    def __init__(self, sort_by, sort_dir=SORT_DIR_ASC):
        self.sort_by = sort_by
        self.sort_dir = sort_dir

    def __repr__(self):
        return f'SortField({self.sort_by}, {self.sort_dir})'


class SortableListMixin:
    default_sort_field = None  # override to set default sorting data
    q_sort_by = 'qSortBy'  # query string param name for the field
    q_sort_dir = 'qSortDir'  # query string param name for sort direction (ascending/descending)

    def get_default_sort_field(self) -> SortField:
        return self.default_sort_field

    def get_ordering(self):
        sf = self.get_default_sort_field()
        orderby = self.request.GET.get(self.q_sort_by, sf.sort_by)
        sort_direction = self.request.GET.get(self.q_sort_dir, sf.sort_dir)

        # The negative sign in front the value indicates descending order.
        if sort_direction == SortField.SORT_DIR_DESC:
            orderby = '-' + orderby
        return orderby

    # keep current sorting url (query string) while paging
    # Example:
    #   <a href='?page={{ page_obj.next_page_number }}&{{ ctx_sort_qstring }}'>next</a>
    #   <a href='?page={{ page_obj.paginator.num_pages }}&{{ ctx_sort_qstring }}'>last</a>
    def get_context_data(self, **kwargs):
        sf = self.get_default_sort_field()
        context = super().get_context_data(**kwargs)
        sort_by = self.request.GET.get(self.q_sort_by, sf.sort_by)
        sort_dir = self.request.GET.get(self.q_sort_dir, sf.sort_dir)
        context['ctx_orderby'] = sort_by
        context['ctx_sort'] = sort_dir
        context['ctx_sort_qstring'] = '&'.join(
            ['='.join([self.q_sort_by, sort_by]), '='.join([self.q_sort_dir, sort_dir])])
        return context
