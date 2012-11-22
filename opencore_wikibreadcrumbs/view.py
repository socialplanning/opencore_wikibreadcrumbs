from opencore.nui.wiki.view import WikiEdit as Base
from opencore.interfaces import IOpenPage

class WikiEdit(Base):
    def blank_slate_content(self):

        project = self.in_project()
        links = []

        if project:
            links.append(
                '<a class="project_home" href="%s">%s</a>' % (
                    project.absolute_url(), project.Title())
                )

        referer = None
        if self.request.form.get('created_from'):
            referer = self.request.form['created_from']
            try:
                referer = IOpenPage(project[referer])
            except (KeyError, TypeError):
                referer = None

        if referer:
            links.append(
                '<a class="created_from" rel="prev" href="%s">%s</a>' % (
                    referer.absolute_url(), referer.Title())
                )

        return "<div class='oc-boxy'>"  + ' | '.join(links) + "</div><hr />" + "<p>Please enter some text for your page</p>"
