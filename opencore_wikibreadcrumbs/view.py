from opencore.nui.wiki.view import WikiEdit as Base

class WikiEdit(Base):
    def blank_slate_content(self):

        project = self.in_project()
        links = []

        if project:
            links.append(
                '<a href="%s">space home: %s</a>' % (
                    project.absolute_url(), project.Title())
                )

        referer = None
        if self.request.form.get('created_from'):
            referer = self.request.form['created_from']
            try:
                referer = project[referer]
            except:
                pass

        if referer:
            links.append(
                '<a href="%s">origin: %s</a>' % (
                    referer.absolute_url(), referer.Title())
                )

        links.append(
            '<a href="%s">site home</a>' % self.portal.absolute_url()
            )
        links.append(
            '<a href="%s/about">help</a>' % self.portal.absolute_url()
            )

        return ' | '.join(links)
