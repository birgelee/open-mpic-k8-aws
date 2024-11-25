terraform {
  required_providers {
    vultr = {
      source  = "vultr/vultr"
      version = "2.11.4"
    }
  }
}

# Configure the Vultr Provider
provider "vultr" {
  rate_limit  = 700
  retry_limit = 3
}


resource "vultr_startup_script" "my_script" {
    name = "init_ssh_key"
    script = filebase64("./startup.sh")
}

# Create an instance
resource "vultr_instance" "vultramsterdam" {
  script_id        = vultr_startup_script.my_script.id
  plan             = "vc2-2c-4gb"
  region           = "ams"
  os_id            = 1743
  backups          = "disabled"
  label            = "vultramsterdam"
  hostname         = "vultramsterdam"
  enable_ipv6      = true
  ddos_protection  = false
  activation_email = false
}


resource "vultr_instance" "vultratlanta" {
  script_id        = vultr_startup_script.my_script.id
  plan             = "vc2-2c-4gb"
  region           = "atl"
  os_id            = 1743
  backups          = "disabled"
  label            = "vultratlanta"
  hostname         = "vultratlanta"
  enable_ipv6      = true
  ddos_protection  = false
  activation_email = false
}

resource "vultr_instance" "vultrchicago" {
  plan             = "vc2-2c-4gb"
  region           = "ord"
  os_id            = 1743
  script_id        = vultr_startup_script.my_script.id
  backups          = "disabled"
  label            = "vultrchicago"
  hostname         = "vultrchicago"
  enable_ipv6      = true
  ddos_protection  = false
  activation_email = false
}