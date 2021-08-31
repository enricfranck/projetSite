from db.models.products import Product
from schemas.products import ProductCreate
from uuid import UUID
from sqlalchemy.orm import Session


def create_new_product(job: ProductCreate, db: Session, owner_id: int):
    product_object = Product(**job.dict(), owner_id=owner_id)
    db.add(product_object)
    db.commit()
    db.refresh(product_object)
    return product_object


def retreive_product(id: UUID, db: Session):
    item = db.query(Product).filter(Product.id == id).first()
    return item


def list_products(db: Session):
    jobs = db.query(Product).all()
    return jobs


def update_product_by_id(id: int, job: ProductCreate, db: Session, owner_id):
    existing_job = db.query(Product).filter(Product.id == id)
    if not existing_job.first():
        return 0
    job.__dict__.update(
        owner_id=owner_id
    )  # update dictionary with new key value of owner_id
    existing_job.update(job.__dict__)
    db.commit()
    return 1


def delete_product_by_id(id: UUID, db: Session, owner_id):
    existing_job = db.query(Product).filter(Product.id == id)
    if not existing_job.first():
        return 0
    existing_job.delete(synchronize_session=False)
    db.commit()
    return 1
