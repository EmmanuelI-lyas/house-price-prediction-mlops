from pydantic import BaseModel


class HouseFeatures(BaseModel):

    MSSubClass: int
    MSZoning: str

    LotFrontage: float | None = None
    LotArea: int

    Street: str
    LotShape: str
    LandContour: str
    Utilities: str
    LotConfig: str
    LandSlope: str

    Neighborhood: str

    Condition1: str
    Condition2: str

    BldgType: str
    HouseStyle: str

    OverallQual: int
    OverallCond: int

    YearBuilt: int
    YearRemodAdd: int

    RoofStyle: str
    RoofMatl: str

    Exterior1st: str
    Exterior2nd: str

    MasVnrType: str | None = None
    MasVnrArea: float | None = None

    ExterQual: str
    ExterCond: str

    Foundation: str

    BsmtQual: str | None = None
    BsmtCond: str | None = None
    BsmtExposure: str | None = None

    BsmtFinType1: str | None = None
    BsmtFinSF1: float

    BsmtFinType2: str | None = None
    BsmtFinSF2: float

    BsmtUnfSF: float
    TotalBsmtSF: float

    Heating: str
    HeatingQC: str
    CentralAir: str

    Electrical: str | None = None

    FirstFlrSF: float
    SecondFlrSF: float
    LowQualFinSF: float

    GrLivArea: float

    BsmtFullBath: int
    BsmtHalfBath: int

    FullBath: int
    HalfBath: int

    BedroomAbvGr: int
    KitchenAbvGr: int

    KitchenQual: str

    TotRmsAbvGrd: int

    Functional: str

    Fireplaces: int

    FireplaceQu: str | None = None

    GarageType: str | None = None
    GarageYrBlt: float | None = None
    GarageFinish: str | None = None

    GarageCars: float
    GarageArea: float

    GarageQual: str | None = None
    GarageCond: str | None = None

    PavedDrive: str

    WoodDeckSF: float
    OpenPorchSF: float
    EnclosedPorch: float

    ThreeSsnPorch: float
    ScreenPorch: float

    PoolArea: float
    MiscVal: float

    MoSold: int
    YrSold: int

    SaleType: str
    SaleCondition: str