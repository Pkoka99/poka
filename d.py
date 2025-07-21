from daytona import Daytona, DaytonaConfig, Resources, Image

# Define your configuration with your actual API key
config = DaytonaConfig(api_key="dtn_d3e4df18b52db372305506f02de7fc79c568a5a33592eed3e65da758ffe55e54")

# Initialize the Daytona client
daytona = Daytona(config)

# Create a new sandbox with 4 vCPUs and Ubuntu (latest version)
sandbox = daytona.create(
    image=Image.ubuntu(),  # ✅ Use latest Ubuntu image
    resources=Resources(
        cpu=4,         # 4 vCPUs
        memory=8,      # 8 GiB RAM
        disk=16        # 16 GiB disk
    )
)

# Run Python code securely inside the sandbox
response = sandbox.process.code_run('print("Hello World from Ubuntu on Daytona 4 vCPU!")')

# Handle the response
if response.exit_code != 0:
    print(f"Error: {response.exit_code} {response.result}")
else:
    print(response.result)
