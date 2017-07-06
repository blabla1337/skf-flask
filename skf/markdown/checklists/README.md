# Checklists

To create a checklist, create a directory here that contains files for each
question to be asked and make a corresponding entry into the `asvs.yaml`
file.

## asvs.yaml

This file contains the list of checklists, and their metadata.

```yaml
checklists:
- id: OWASP-level-2:
  title: OWASP ASVS Level 2
  description: OWASP Application Security Verification Standard Level 2
  level: Recommended
```

This is an ordered list of each checklist, and the information needed to
properly display it. The checklist's key (`OWASP-level-2` above) is used
as the name of the directory that should contain the checklist's questions.

## Questions

Each question is read from its own file. These files must be named
correctly.

```
001--61--yg.md
^^^  ^^  ^^ ^- questions are provided as markdown files
|    |   |
|    |   ^- ygb badges
|    |
|    ^- knowledge base reference(s)
|
^- question index
```

Examples:
```
13th item with green and blue badge, described by KB #70
013--70--gb.md

157th item, described by Knowledge Base entried #60, #14
157--60--14.md

First item in checklist, section heading
001--0.md
```

### Question index

The question index is used to order the questions, and to look up the
question's content when displaying reports.

### Knowledge base reference(s)

You may provide knowledge base IDs that will be used as a description for
the question when the checklist is displayed. These should correspond to
the number at the start of the knowledge base entry's file.

You can provide any number of knowledge base references, but the UI is
optimised for a single entry.

### YGB badges

Some checklists (such as the OWASP ASVS checklists) may be available at
multiple levels. To help visually convey which questions are at which
level you may choose to include YGB badges on questions. These must be
at the end of the filename, and can only include one or more of the
characters `y`, `g` and `b`.

## Section headings

Section headings are put into the checklist's display when an item uses
`0` in place of its knowledge base reference.
