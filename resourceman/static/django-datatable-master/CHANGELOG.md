## v0.2.1
* Fix error about loading ajax data when serving requests with multiple processes in production env.

## v0.2.0
* Added compatibility with Python 3
* Make checkboxfield related to object field.
* Added ImageColumn

## v0.1.5

* PyPi support

## v0.1.4
* Fix bug about escape issue for ajax data source.

## v0.1.3
* Fix bug about sorting field across different relations.

## v0.1.2
* New columns:

    * SequenceColumn
    * DaysColumn
    * WeeksColumn
    * MonthColumn
    * CalendarColumn
    * CheckboxColumn

* New column options:

    * space

* Refactoring table module
* Support subclass table

## v0.1.1

* New column:

    * DatetimeColumn

* New options to disable widgets

    * search
    * info
    * pagination
    * length_menu
    * ext_button

* Fix bug about filtering href columns, ignore text of HTML tag.

## v0.1.0

First commit for codebase.

## v0.3.0

* Deprecate table option `ext_button`.
* Make table template inheritable.

## v.0.3.1
* Fix bug about template context, campatible with Django 1.10 & 1.11.
