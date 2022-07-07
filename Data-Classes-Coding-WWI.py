from dataclasses import dataclass, field
from datetime import date, datetime
import string

@dataclass
class Orders:
    OrderID: int
    CustomerID: int
    SalespersonPersonID: int
    PickedByPersonID: int
    ContactPersonID: int
    BackorderOrderID: int
    OrderDate: date
    ExpectedDeliveryDate: date
    CustomerPurchaseOrderNumber: string
    IsUndersupplyBackordered: bool
    Comments: string
    DeliveryInstructions: string
    InternalComments: string
    PickingCompletedWhen: datetime
    LastEditedBy: int
    LastEditedWhen: datetime

    def __gt__(self,other):
        return self.OrderID > other.OrderID
    
    def __ge__(self,other):
        return self.OrderID >= other.OrderID


@dataclass
class Invoices:
    InvoiceID: int
    CustomerID: int
    BillToCustomerID: int
    OrderID: int
    DeliveryMethodID: int
    ContactPersonID: int
    AccountsPersonID: int
    SalespersonPersonID: int
    PackedByPersonID: int
    InvoiceDate: date
    CustomerPurchaseOrderNumber: string
    IsCreditNote: bool
    CreditNoteReason: string
    Comments: string
    DeliveryInstructions: string
    InternalComments: string
    TotalDryItems: int
    TotalChillerItems: int
    DeliveryRun: string
    RunPosition: string
    ReturnedDeliveryData: string
    ConfirmedDeliveryTime: datetime
    ConfirmedReceivedBy: string
    LastEditedBy: int
    LastEditedWhen: datetime

    def __gt__(self,other):
        return self.InvoiceID > other.InvoiceID
    
    def __ge__(self,other):
        return self.InvoiceID >= other.InvoiceID


@dataclass
class Customers:
    CustomerID: int
    CustomerName: string
    BillToCustomer: int
    CustomerCategoryID: int
    BuyingGroupID: int
    PrimaryContactPersonID: int
    AlternateContactPersonID: int
    DeliveryMethodID: int
    DeliveryCityID: int
    PostalCityID: int
    CreditLimit: float
    AccountOpenedDate: date
    StandardDiscountPercentage: float
    IsStatementSent: bool
    IsOnCreditHold: bool
    PaymentDays: int
    PhoneNumber: string
    FaxNumber: string
    DeliveryRun: string
    RunPosition: string
    WebsiteURL: string
    DeliveryAddressLine1: string
    DeliveryAddressLine2: string
    DeliveryPostalCode: string
    DeliveryLocation: string
    PostalAddressLine1: string
    PostalAddressLine2: string
    PostalPostalCode: string
    LastEditedBy: int
    ValidFrom: datetime
    ValidTo: datetime