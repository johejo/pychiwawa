class AttributeDict(object):
    def __init__(self, obj):
        self.obj = obj

    def __getstate__(self):
        return self.obj.items()

    def __setstate__(self, items):
        if not hasattr(self, 'obj'):
            self.obj = {}
        for key, val in items:
            self.obj[key] = val

    def __getattr__(self, name):
        if name in self.obj:
            return self.obj.get(name)
        else:
            return None

    def fields(self):
        return self.obj

    def keys(self):
        return self.obj.keys()


# This class is under construction.
class ChiwawaAttachmentsObj(object):
    def __init__(self, attachment_id,
                 *, view_type=None, title=None, text=None,
                 text_in_timeline=None, line_break_in_timeline=None,
                 text_type=None, color=None, tag_icons=None,
                 display_comment_field=None, comment_field=None,
                 actions=None, ):
        self.attachment_id = attachment_id
        self.view_type = view_type
        self.title = title
        self.text = text
        self.text_in_timeline = text_in_timeline
        self.line_break_in_timeline = line_break_in_timeline
        self.text_type = text_type
        self.color = color
        self.tag_icons = tag_icons
        self.display_comment_field = display_comment_field
        self.comment_field = comment_field
        self.actions = actions

    def to_dict(self):
        d = {'attachmentId': self.attachment_id}

        if self.view_type is not None:
            d['viewType'] = self.view_type

        if self.title is not None:
            d['title'] = self.title

        if self.text is not None:
            d['text'] = self.text

        if self.text_in_timeline is not None:
            d['textInLine'] = self.text_in_timeline

        if self.line_break_in_timeline is not None:
            d['lineBrakeInTimeline'] = self.line_break_in_timeline
        else:
            d['lineBrakeInTimeline'] = 'none'

        if self.text_type is not None:
            d['textType'] = self.text_type
        else:
            d['textType'] = 'none'

        if self.color is not None:
            d['color'] = self.color

        if self.tag_icons is not None:
            d['tagIcon'] = self.tag_icons

        if self.display_comment_field is not None:
            d['displayCommentField'] = self.display_comment_field

        if self.comment_field is not None:
            d['commentField'] = self.comment_field

        if self.actions is not None:
            d['actions'] = self.actions

        return d


class ChiwawaActionsObj(object):
    def __init__(self, *, button_title=None, localized_title=None,
                 dislays_in='both',
                 action_url, auth_type, action_type, post_body,
                 post_body_content_type):
        self.button_title = button_title
        self.localized_title = localized_title
        self.displays_in = dislays_in
        self.action_url = action_url
        self.auth_type = auth_type
        self.action_type = action_type
        self.post_body = post_body
        self.post_body_content_type = post_body_content_type

    def to_dict(self):
        d = {}

        if self.button_title is not None:
            d['buttonFiled'] = self.button_title

        if self.localized_title is not None:
            d['localizedTile'] = self.localized_title

        if self.displays_in is not None:
            d['displaysIn'] = self.displays_in

        if self.action_url is not None:
            d['actionUrl'] = self.action_url

        if self.action_type is not None:
            d['actionType'] = self.action_type

        if self.auth_type is not None:
            d['authType'] = self.auth_type

        if self.post_body is not None:
            d['postBody'] = self.post_body

        if self.post_body_content_type is not None:
            d['postBodyContentType'] = self.post_body_content_type

        return d
