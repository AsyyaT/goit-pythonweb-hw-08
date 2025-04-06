from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db import get_db
from src.repository import contacts
from src.schemas import ContactCreate, ContactUpdate

router = APIRouter(prefix="/contacts", tags=["contacts"])

CONTACT_NOT_FOUND = "Contact not found"


@router.post("/", response_model=ContactCreate)
def add_contact(contact: ContactCreate, db: Session = Depends(get_db)):
    try:
        return contacts.create_contact(db, contact)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/")
def get_contacts(name: str = None, email: str = None, db: Session = Depends(get_db)):
    return contacts.get_contacts(db, name, email)


@router.get("/{contact_id}")
def get_contact_by_id(contact_id: int, db: Session = Depends(get_db)):
    contact = contacts.get_contact(db, contact_id)
    if not contact:
        raise HTTPException(status_code=404, detail=CONTACT_NOT_FOUND)

    return contact


@router.put("/{contact_id}")
def update_contact(contact_id: int, contact_update: ContactUpdate, db: Session = Depends(get_db)):
    updated_contact = contacts.update_contact(db, contact_id, contact_update)
    if not updated_contact:
        raise HTTPException(status_code=404, detail=CONTACT_NOT_FOUND)

    return updated_contact


@router.delete("/{contact_id}")
def delete_contact(contact_id: int, db: Session = Depends(get_db)):
    deleted_contact = contacts.delete_contact(db, contact_id)
    if not deleted_contact:
        raise HTTPException(status_code=404, detail=CONTACT_NOT_FOUND)

    return {"detail": "Contact deleted"}
