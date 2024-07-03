from clients import antropic_client


def get_natal_map(name, birth_date, birth_time, birth_location):
    message = antropic_client.messages.create(
        max_tokens=4096,
        messages=[
            {
                "role": "user",
                "content": f'''
Создай детальную натальную карту, с пояснениями и описаниями характеристик для этого человека.
Имя: {name}
Дата рождения: {birth_date}
Время рождения: {birth_time}
Место рождения: {birth_location}
'''
            },
        ],
        model="claude-3-haiku-20240307",
    )
    return message.content[0].text
