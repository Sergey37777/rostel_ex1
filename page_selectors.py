class Selectors:
    inn = '//div[text()="ИНН"]/following-sibling::div/text()'  # ИНН
    kpp = '//div[text()="КПП"]/following-sibling::div/text()'  # КПП
    ceo_name = '.contractorCard-Chief__fullName-readOnly'  # ФИО ГД
    position = '[data-qa="ContractorCard-Chief_jobTitle"]'  # Должность ГД
    phone_number = '.icon-PhoneWork+.contractorCard-ContactItem .contractorCard-ContactItem__text'  # Телефон
    email = '.icon-EmailNew+.contractorCard-ContactItem .contractorCard-ContactItem__text'  # Email
    website = '.icon-WWW+.contractorCard-ContactItem .contractorCard-ContactItem__text'  # Сайт