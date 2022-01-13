import re

def email_parse(mail_addr='email@email.com'):
    if re.match(r"^[\w-]+@([\w-]+\.)+[\w-]{2,4}$", mail_addr) is not None:
        print({'username': mail_addr.split('@')[0], 'domain': mail_addr.split('@')[-1]})
    else:
        raise ValueError(f'Wrong email: {mail_addr}')

email_parse('hochu_v_otpusk@mail.ru')
