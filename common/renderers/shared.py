"""
Objects that are shared among the renderers
"""


class DownloadMixin(object):
    extension = None

    def update_download_headers(self, renderer_context):
        view = renderer_context.get('view')
        fname = view.get_view_name() or 'download'

        fname = "{}.{}".format(fname, self.extension)
        view.response._headers['content-disposition'] = (
            'Content-Disposition',
            'attachment; filename="{}"'.format(fname)
        )
