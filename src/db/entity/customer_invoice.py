from data import Base
from sqlalchemy import Column, Integer, ForeignKey


class CustomerInvoice(Base):

    __tablename__ = "CustomerInvoice"

    id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey("Customer.id"), nullable=False)
    invoice_id = Column(Integer, ForeignKey("Invoice.id"), nullable=False)
