---
layout: post
title: Small Django patch to add full traceback for wrapper exception during template rendering
published: true
---

Here is a patch that I'm tending to apply to my Django (currently v1.1.1)
tree to give me a full traceback on the wrapped exception when getting an
exception during template processing. Without this patch you only get
the string summary of the underlying exception -- often far from enough info
to track down the actual bug. With this patch the result isn't that pretty (a full Python traceback as the string summary of the TemplateSyntaxError), but the info sure is helpful.

    Index: debug.py
    ===================================================================
    --- debug.py	(revision 11742)
    +++ debug.py	(working copy)
    @@ -68,20 +68,23 @@
     class DebugNodeList(NodeList):
         def render_node(self, node, context):
             try:
                 result = node.render(context)
             except TemplateSyntaxError, e:
                 if not hasattr(e, 'source'):
                     e.source = node.source
                 raise
             except Exception, e:
                 from sys import exc_info
    +            #TODO?: grab the "(at $file:$line)" suffix code, tack that on, propose for Django core
    +            import traceback
    +            e = traceback.format_exc()
                 wrapped = TemplateSyntaxError(u'Caught an exception while rendering: %s' % force_unicode(e, errors='replace'))
                 wrapped.source = node.source
                 wrapped.exc_info = exc_info()
                 raise wrapped
             return result
     
     class DebugVariableNode(VariableNode):
         def render(self, context):
             try:
                 output = force_unicode(self.filter_expression.resolve(context))

