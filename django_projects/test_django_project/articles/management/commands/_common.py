from faker import Faker


rubrics_with_tags = {
    "Computer science": (
        "windows", "linux", "macos", "android", "ios", "pc", "hardware", "software"
    ),
    "Automobiles": (
        "sport cars", "racing", "cars", "rally", "formula 1"
    ),
    "Space": (
        "space", "planet", "star", "Sun", "Earth", "moon", "asteroid", "cosmonaut", "meteorite"
    ),
    "Books": (
        "book", "travel book", "fantasy book", "story", "detective story", "fairy tale", "legend", "library"
    ),
    "Sports": (
        "team", "coach", "referee", "championship", "tournament", "victory", "defeat", "draw"
    ),
}


faker = Faker()


def get_jobs(amount):
    return [faker.job() for _ in range(amount)]


def get_names(amount):
    return [faker.name() for _ in range(amount)]


def get_emails(amount):
    return [faker.email() for _ in range(amount)]


def get_title(words=3):
    return faker.sentence(nb_words=words, variable_nb_words=False)


def get_content(sentences=20):
    return faker.paragraph(nb_sentences=sentences)
