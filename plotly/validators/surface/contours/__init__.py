import _plotly_utils.basevalidators


class ZValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="z", parent_name="surface.contours", **kwargs):
        super(ZValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Z"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            color
                Sets the color of the contour lines.
            end
                Sets the end contour level value. Must be more
                than `contours.start`
            highlight
                Determines whether or not contour lines about
                the z dimension are highlighted on hover.
            highlightcolor
                Sets the color of the highlighted contour
                lines.
            highlightwidth
                Sets the width of the highlighted contour
                lines.
            project
                plotly.graph_objects.surface.contours.z.Project
                instance or dict with compatible properties
            show
                Determines whether or not contour lines about
                the z dimension are drawn.
            size
                Sets the step between each contour level. Must
                be positive.
            start
                Sets the starting contour level value. Must be
                less than `contours.end`
            usecolormap
                An alternate to "color". Determines whether or
                not the contour lines are colored using the
                trace "colorscale".
            width
                Sets the width of the contour lines.
""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class YValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="y", parent_name="surface.contours", **kwargs):
        super(YValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Y"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            color
                Sets the color of the contour lines.
            end
                Sets the end contour level value. Must be more
                than `contours.start`
            highlight
                Determines whether or not contour lines about
                the y dimension are highlighted on hover.
            highlightcolor
                Sets the color of the highlighted contour
                lines.
            highlightwidth
                Sets the width of the highlighted contour
                lines.
            project
                plotly.graph_objects.surface.contours.y.Project
                instance or dict with compatible properties
            show
                Determines whether or not contour lines about
                the y dimension are drawn.
            size
                Sets the step between each contour level. Must
                be positive.
            start
                Sets the starting contour level value. Must be
                less than `contours.end`
            usecolormap
                An alternate to "color". Determines whether or
                not the contour lines are colored using the
                trace "colorscale".
            width
                Sets the width of the contour lines.
""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class XValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="x", parent_name="surface.contours", **kwargs):
        super(XValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "X"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            color
                Sets the color of the contour lines.
            end
                Sets the end contour level value. Must be more
                than `contours.start`
            highlight
                Determines whether or not contour lines about
                the x dimension are highlighted on hover.
            highlightcolor
                Sets the color of the highlighted contour
                lines.
            highlightwidth
                Sets the width of the highlighted contour
                lines.
            project
                plotly.graph_objects.surface.contours.x.Project
                instance or dict with compatible properties
            show
                Determines whether or not contour lines about
                the x dimension are drawn.
            size
                Sets the step between each contour level. Must
                be positive.
            start
                Sets the starting contour level value. Must be
                less than `contours.end`
            usecolormap
                An alternate to "color". Determines whether or
                not the contour lines are colored using the
                trace "colorscale".
            width
                Sets the width of the contour lines.
""",
            ),
            **kwargs
        )
