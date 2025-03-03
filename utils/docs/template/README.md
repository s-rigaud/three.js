# Template structure

## Layout


layout.tmpl
    -> search.tmpl
    -> (content)
        -> container.tmpl (class/module/code level)

            # dark page
            -> mainpage.tmpl

            # code
            -> source.tmpl

            #class detail
            -> method.tmpl
                -> params.tmpl
                -> exception.tmpl
                -> type.tmpl
            -> detail.tmpl
            -> example.tmpl
            -> augments.tmpl
            -> members.tmpl

# Being called a bit everywhere as a placeholder
-> type.tmpl
