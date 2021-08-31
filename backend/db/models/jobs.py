from db.base_class import Base
from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import Date
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4


class Job(Base):
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    title = Column(String, nullable=False)
    company = Column(String, nullable=False)
    company_url = Column(String)
    location = Column(String, nullable=False)
    description = Column(String, nullable=False)
    date_posted = Column(Date)
    is_active = Column(Boolean(), default=True)
    owner_id = Column(UUID(as_uuid=True), ForeignKey("user.id"))
    owner = relationship("User", back_populates="jobs")
