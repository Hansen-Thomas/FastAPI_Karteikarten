from domain.tag.tag import Tag


def get_tag1() -> Tag:
    tag = Tag(value="Natur")
    return tag


def get_tag2() -> Tag:
    tag = Tag(value="Verkehr")
    return tag


def get_tag3() -> Tag:
    tag = Tag(value="Beruf")
    return tag


def get_test_tags() -> list[Tag]:
    return [get_tag1(), get_tag2(), get_tag3()]