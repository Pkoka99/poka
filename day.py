from daytona import Daytona, CreateSnapshotParams, Image, Resources

daytona = Daytona()

daytona.snapshot.create(
    CreateSnapshotParams(
        name="snapshot-4vcpu",
        image=Image.debian_slim("3.12"),
        resources=Resources(
            cpu=4,         # <-- 4 vCPUs
            memory=8,      # e.g., 8 GiB RAM
            disk=16,       # e.g., 16 GiB disk
        ),
    ),
    on_logs=print,
)
