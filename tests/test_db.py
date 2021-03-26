from smartmail.models.contact import ContactModel
from smartmail.models.tag import TagModel
from smartmail.models.case import CaseModel

def test_contactmodel_save(app):
    with app.app_context():
        contact = ContactModel(first_name="John", last_name="Doe", email="john_doe@gmail.com", phone="8117266267")
        contact.save_to_db()
        assert ContactModel.find_by_email('john_doe@gmail.com')

def test_tagmodel_save(app):
    with app.app_context():
        tag = TagModel(title="To be resolved", color="red")
        tag.save_to_db()
        assert TagModel.find_by_title('To be resolved')

def test_casemodel_save(app):
    with app.app_context():
        case = CaseModel(title="Car accident", description="car accident that damaged the car", tag_id=1, contact_id=1)
        case.save_to_db()
        assert CaseModel.find_by_title('Car accident')

def test_contactmodel_all(app):
    with app.app_context():
        assert ContactModel.find_all()

def test_tagmodel_all(app):
    with app.app_context():
        assert TagModel.find_all()

def test_casemodel_all(app):
    with app.app_context():
        assert CaseModel.find_all()

def test_casemodel_delete(app):
    with app.app_context():
        case = CaseModel.find_by_title('Car accident')
        case.delete_from_db() 
        assert CaseModel.find_by_title('Car accident') == None

def test_tagmodel_delete(app):
    with app.app_context():
        tag = TagModel.find_by_title('To be resolved')
        tag.delete_from_db() 
        assert TagModel.find_by_title('To be resolved') == None

def test_contactmodel_delete(app):
    with app.app_context():
        contact = ContactModel.find_by_email('john_doe@gmail.com')
        contact.delete_from_db() 
        assert ContactModel.find_by_email('john_doe@gmail.com') == None
